#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - Inserts a number into a sorted singly linked list.
 * @head: Double pointer to a singly linked list
 * @number: Value of the new node.
 * Return: The address  or NULL
 */

listint_t *insert_node(listint_t **head, int number)
{
	int flag = 0;
	listint_t *newNode = NULL, *thisNode = NULL, *nextOp = NULL;

	if (head == NULL)
		return (NULL);
	newNode = malloc(sizeof(listint_t));

	if (!newNode)
		return (NULL);
	newNode->n = number, newNode->next = NULL;

	if (*head == NULL)
	{
		*head = newNode;
		return (*head);
	}
	thisNode = *head;

	if (number <= thisNode->n)
	{
		newNode->next = thisNode, *head = newNode;
		return (*head);
	}

	if (number > thisNode->n && !thisNode->next)
	{
		thisNode->next = newNode;
		return (newNode);
	}
	thisNode = thisNode->next;

	while (thisNode)
	{
		if (!nextOp)
			thisNode->next = newNode, flag = 1;
		else if (NextOp->n == number)
			thisNode->next = newNode, newNode->next = nextOp, flag = 1;
		else if (nextOp->n > number && thisNode->n < number)
			thisNode->next = newNode, newNode->next = nextOp, flag = 1;
		if (flag)
			break;
		NextOp = nextOp->next, thisNode = thisNode->next;
	}
	return (newNode);
}
