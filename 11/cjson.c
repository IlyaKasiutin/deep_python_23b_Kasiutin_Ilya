#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <python3.10/Python.h>


PyObject* process_token(char* token)
{
    if (token[0] == '\"' && token[strlen(token) - 1] == '\"')
    {
        // printf("TOKEN_PROCESS: %s\n", token);
        size_t len = strlen(token);
        token[len-1] = '\0';
        // char new_token[len - 2];
        // strncpy(new_token, token + 1, len - 2);
        // printf("TOKEN End: %s\n", new_token);
        // printf("TOKEN LEN: %d\n", len - 2);
        return Py_BuildValue("s", token + 1);
    }
    
    else if (token[0] != '\"' && token[1] != '\"')
    {
        for (int i = 0; i < strlen(token); i++)
        {
            if (!isalpha(token[i]))
                PyErr_Format(PyExc_TypeError, "Expected str or int");

        }
        printf("DIGIT: %s\n", token);
        printf("LEN: %d\n", strlen(token));
        // int val = atoi(token);
        // printf("VAL: %s\n", val);
        return Py_BuildValue("i", token);
    }
    
    else
        PyErr_Format(PyExc_TypeError, "Expected str or int");
}



PyObject* loads(PyObject* self, PyObject* args)
{
    char* json_base_str = NULL;
    if (!PyArg_ParseTuple(args, "s", &json_base_str))
    {
        PyErr_Format(PyExc_TypeError, "Expected object or value\n");
        return NULL;
    }
    printf("JSON_BASE_STR: %s\n", json_base_str);

    size_t len = strlen(json_base_str);
    printf("STRLEN: %d\n", len);
    if (json_base_str[0] != '{' && json_base_str[len - 2] != '}')
    {
        PyErr_Format(PyExc_TypeError, "Expected json string");
    }
    json_base_str[len - 1] = '\0';
    printf("UPDATED STR: %s\n", json_base_str);

    char json_str[len];
    strncpy(json_str, json_base_str + 1, len - 1);
    printf("JSON_STR: %s\n", json_str);


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
        printf("TOKEN: %s\n", token);
        if (key == NULL)
            key = process_token(token);
        else if (value == NULL)
        {
            value = process_token(token);
            puts("INSERTING...");
            // value = Py_BuildValue("s", value);
            // key = Py_BuildValue("s", key);

            // printf("KEY: %s, VALUE: %s\n", key, value);
            PyDict_SetItem(dict, key, value);
            puts("FINISHED INSERT");
            key = NULL;
            value = NULL;
        }
        token = strtok(NULL, ":, ");
    }
    return dict;
}

static PyMethodDef methods[] = {
    {"loads", loads, METH_VARARGS, "parse json-string into python dict"}
};


static struct PyModuleDef module_json = {
    PyModuleDef_HEAD_INIT, "cjson", NULL, -1, methods
};

PyMODINIT_FUNC 
PyInit_cjson()
{
    return PyModule_Create(&module_json);
}
