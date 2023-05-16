#include <Python.h>
#include <object.h>
#include <listobject.h>

/**
 * print_python_list_info - Prints information about a Python list object
 * @p: A pointer to a Python list object
 *
 * This function prints the length of the list, the amount of allocated memory,
 * and the type of each element in the list.
 */
void print_python_list_info(PyObject *p)
{
	Py_ssize_t size, i;
	PyListObject *list = (PyListObject *)p;

	size = list->ob_base.ob_size;
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", list->allocated);
	for (i = 0; i < size; i++)
		printf("Element %ld: %s\n", i, list->ob_item[i]->ob_type->tp_name);
}
