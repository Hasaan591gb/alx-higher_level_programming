#include <stdio.h>
#include "lists.h"

/**
 * check_palindrome - recursively checks if a linked list is a palindrome
 * @current: double pointer to the current node
 * @right: pointer to the rightmost node
 *
 * Return: 1 if the list is a palindrome, 0 otherwise
 */
int check_palindrome(listint_t **current, listint_t *right)
{
	int ispal;

	if (right == NULL)
		return (1);

	ispal = check_palindrome(current, right->next);
	if (ispal)
	{
		if ((*current)->n != right->n)
			ispal = 0;
		*current = (*current)->next;
	}

	return (ispal);
}

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: double pointer to the head of the list
 *
 * Return: 1 if the list is a palindrome, 0 otherwise
 */
int is_palindrome(listint_t **head)
{
	if (*head == NULL || (*head)->next == NULL)
		return (1);

	return (check_palindrome(head, *head));
}
