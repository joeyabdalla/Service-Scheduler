#include <Python.h>

// Your C functions here ...
int multiply(int a, int b);


static PyObject* py_multiply(PyObject* self, PyObject* args) {
    int a, b;
    if (!PyArg_ParseTuple(args, "ii", &a, &b)) {
        return NULL;
    }
    return Py_BuildValue("i", multiply(a, b));
}

static PyMethodDef methods[] = {
    {"multiply", py_multiply, METH_VARARGS, "Multiply two integers"},
    {NULL, NULL, 0, NULL}
};

static struct PyModuleDef operationsmodule = {
    PyModuleDef_HEAD_INIT, "operations", NULL, -1, methods
};

PyMODINIT_FUNC PyInit_operations(void) {
    return PyModule_Create(&operationsmodule);
}
