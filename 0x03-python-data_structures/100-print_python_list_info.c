#include <stdio.h>
#include <Python.h>
/**
 * print_python_list_info - prints python list info
 * @p: The PyObject list
*/
void print_python_list_info(PyObject *p)
{
	int size, alloc, i;
	PyObject *item;
	char *type1;

	if (PyList_Check(p))
	{
		size  = Py_SIZE(p);
		alloc = ((PyListObject *)p)->allocated;
		printf("[*] Size of the Python List = %d\n", size);
		printf("[*] Allocated = %d\n", alloc);
		for (i = 0; i < size; i++)
		{
			item = PyList_GET_ITEM(p, i);
			type = PyTYPE(item)->tp_name;
			printf("Element %d: %s\n", i, type1);
		}
	}
}
