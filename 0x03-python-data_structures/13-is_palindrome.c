#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

size_t count_nodes(listint_t *node);

/**
 * is_palindrome - Checks if a singly linked list is a palindrome
 * @head: Double pointer to the head of the linked list
 *
 * Return: 0 if the list is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *current = *head;
	size_t node_num;
	int *array;
	size_t i, palid_check = 1;

	if (head == NULL)
		return (0);

	node_num = count_nodes(current);
	array = malloc(sizeof(int) * node_num);
	if (array == NULL)
		return (0);

	for (i = 0; i < node_num; i++)
	{
		*(array + i) = current->n;
		current = current->next;
	}

	for (i = 0; i < (node_num / 2); i++)
	{
		if (*(array + i) != *(array + (node_num - i - 1)))
		{
			palid_check = 0;
			break;
		}
	}

	free(array);
	return (palid_check);
}

/**
 * count_nodes - Counts the number of nodes in a linked list
 * @node: Pointer to the head of the linked list
 *
 * Return: The number of nodes in the linked list
 */
size_t count_nodes(listint_t *node)
{
	size_t n = 0;

	while (node != NULL)
	{
		n++;
		node = node->next;
	}

	return (n);
}
