#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - inserts a number into a sorted singly linked list
 * @head: double pointer to the head of the list
 * @number: the number to insert
 *
 * Return: the address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current, *new, *tmp;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;
	new->next = NULL;

	if (*head == NULL)
		*head = new;
	else
	{
		current = *head;
		tmp = *head;
		while (current->n < number)
		{
			if (current->next == NULL)
			{
				current->next = new;
				return (new);
			}
			tmp = current;
			current = current->next;
		}
		new->next = tmp->next;
		tmp->next = new;
	}

	return (new);
}
