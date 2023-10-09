#include <Python.h>
/**
 * print_python_list_info - prints python list info
 * @p: The PyObject list
*/
void print_python_list_info(PyObject *p)
{
	int size, alloc, i;
	PyObject *item;

	size  = Py_SIZE(p);
	alloc = ((PyListObject *)p)->allocated;
	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", alloc);
	for (i = 0; i < size; i++)
	{
		item = PyList_GET_ITEM(p, i);
		printf("Element %d: %s\n", i, Py_TYPE(item)->tp_name);
	}
}
