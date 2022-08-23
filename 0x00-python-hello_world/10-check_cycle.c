#include "lists.h"

/**
 * check_cycle - checks for a cycle in a singly linked
 * @list: pointer to the list
 * Return: 0 or 1
 */

int check_cycle(listint_t *list)
{
	listint_t *cycle;
	listint_t *check;

	cycle = list;
	check = list;
	while (list && cycle && cycle->next)
	{
		list = list->next;
		cycle = cycle->next->next;

		if (list == cycle)
		{
			list = check;
			check =  cycle;
			while (1)
			{
				cycle = check;
				while (cycle->next != list && cycle->next != check)
				{
					cycle = cycle->next;
				}
				if (cycle->next == list)
					break;

				list = list->next;
			}
			return (1);
		}
	}

	return (0);
}
