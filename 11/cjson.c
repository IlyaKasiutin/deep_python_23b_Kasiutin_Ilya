#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <python3.10/Python.h>


PyObject* process_token(char* token)
{
    if (token[0] == '\"' && token[strlen(token) - 1] == '\"')
    {
        size_t len = strlen(token);
        char new_token[len-1];
        new_token[len - 2] = '\0';
        strncpy(new_token, token + 1, len - 2);
        return Py_BuildValue("s", new_token);
    }
    
    else if (token[0] != '\"' && token[strlen(token) - 1] != '\"')
    {
        size_t len = strlen(token);
        for (size_t i = 0; i < len; i++)
        {
            if (!isdigit(token[i]))
                return NULL;

        }

        int val = atoi(token);
        return Py_BuildValue("i", val);
    }
    
    return NULL;
}

int check_key_token(const char* string)
{
    return (string[0] == '\"' && string[strlen(string) - 1] == '\"');
}

PyObject* loads(PyObject* self, PyObject* args)
{
    char* json_base_str = NULL;
    if (!PyArg_ParseTuple(args, "s", &json_base_str))
    {
        PyErr_Format(PyExc_TypeError, "Expected object or value\n");
        return NULL;
    }

    size_t len = strlen(json_base_str);

    if (json_base_str[0] != '{' && json_base_str[len - 2] != '}')
    {
        PyErr_Format(PyExc_TypeError, "Expected json string");
    }

    char json_str[len - 2];
    strncpy(json_str, json_base_str + 1, len - 2);
    json_str[len - 2] = '\0';


    PyObject* dict = NULL;
    if (!(dict = PyDict_New()))
    {
        PyErr_Format(PyExc_MemoryError, "Failed to create Dict Object\n");
        return NULL;
    }

    PyObject* key = NULL;
    PyObject* value = NULL;
    char* token = strtok(json_str, ":, ");


    while (token != NULL)
    {
        if (key == NULL)
        {
            if (!check_key_token(token))
            {
                PyErr_Format(PyExc_TypeError, "Expected object or value\n");
                return NULL;
            }
            key = process_token(token);
        }
            
        else if (value == NULL)
        {
            value = process_token(token);
            if (key == NULL || value == NULL)
            {
                PyErr_Format(PyExc_TypeError, "Expected object or value\n");
                return NULL;
            }


            PyDict_SetItem(dict, key, value);
            key = NULL;
            value = NULL;
        }
        token = strtok(NULL, ":, ");
    }
    return dict;
}


const char* string_from_pyobject(PyObject* pyobject)
{
    PyObject* repr = PyObject_Repr(pyobject);
    PyObject* str = PyUnicode_AsEncodedString(repr, "utf-8", "~E~");
    char *string = PyBytes_AS_STRING(str);
    return string;
}


int is_str(PyObject* pyobject)
{
    return PyUnicode_Check(pyobject);
}

int is_int(PyObject* pyobject)
{
    return PyLong_CheckExact(pyobject);
}

int is_dict(PyObject* pyobject)
{
    return PyDict_CheckExact(pyobject);
}

char* replace_char(char* str, char find, char replace){
    char *current_pos = strchr(str,find);
    while (current_pos) {
        *current_pos = replace;
        current_pos = strchr(current_pos,find);
    }
    return str;
}


PyObject* dumps(PyObject* self, PyObject* args)
{
    PyObject* json_dict = NULL;
    if (!PyArg_ParseTuple(args, "O", &json_dict))
    {
        PyErr_Format(PyExc_TypeError, "Expected object or value\n");
        return NULL;
    }

    if (!is_dict(json_dict))
    {
        PyErr_Format(PyExc_TypeError, "Expected object or value\n");
        return NULL;
    }

    PyObject *key;
    PyObject *value;
    Py_ssize_t pos = 0;

    while (PyDict_Next(json_dict, &pos, &key, &value))
    {
        if (!is_str(key))
        {
            PyErr_Format(PyExc_TypeError, "Expected object or value\n");
            return NULL;
        }

        if (!is_int(value) && !is_str(value))
        {
            PyErr_Format(PyExc_TypeError, "Expected object or value\n");
            return NULL;
        }  
    }

    char* str_repr = string_from_pyobject(json_dict);
    replace_char(str_repr, '\'', '\"');
    return Py_BuildValue("s", str_repr);
}


static PyMethodDef methods[] = {
    {"loads", loads, METH_VARARGS, "parse json-string into python dict"},
    {"dumps", dumps, METH_VARARGS, "parse json-dict into str"}
};


static struct PyModuleDef module_json = {
    PyModuleDef_HEAD_INIT, "cjson", NULL, -1, methods
};

PyMODINIT_FUNC 
PyInit_cjson()
{
    return PyModule_Create(&module_json);
}
