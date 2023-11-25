#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "C:\Users\user\AppData\Local\Programs\Python\Python39\include\Python.h"


PyObject* loads(PyObject* self, PyObject* args)
{
    char* json_base_str;
    if (!PyArg_Parse(args, "s", json_base_str))
    {
        PyErr_Format(PyExc_TypeError, "Expected object or value\n");
        return NULL;
    }

    size_t len = strlen(json_base_str);
    if (json_base_str[0] != '{' && json_base_str[len - 2] != '}')
    {
        PyErr_Format(PyExc_TypeError, "Expected json string");
    }
    json_base_str[len - 2] = '\0';

    char json_str[len];
    strncpy(json_str, json_base_str + 1, len - 1);


    PyObject* dict = NULL;
    if (!(dict = PyDict_New()))
    {
        PyErr_Format(PyExc_MemoryError, "Failed to create Dict Object\n");
        return NULL;
    }

    PyObject* key = NULL;
    PyObject* value = NULL;
    char* token = strtok(json_str + 1, ":, ");
    while (token != NULL)
    {
        if (key == NULL)
            key = token;
        else if (value == NULL)
        {
            value = token;
            PyDict_SetItem(dict, key, value);
            key = NULL;
            value = NULL;
        }
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
