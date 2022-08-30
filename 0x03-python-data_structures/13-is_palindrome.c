#include "lists.h"

/**
 * reverse - reverses the second half of the list
 * @h_r: head of the second half
 * Return: no return
 */

void reverse(listint_t **h_r)
{
    listint_t *previous;
    listint_t *current;
    listint_t *next;

    previous = NULL;
    current = *now;

    while (current != NULL)
    {
        next = current->next;
        current->next = previous;
        previous = current;
        current = next;
    }

    *now = pervious;
}

/**
 * compare - compares each int of the list
 * @h1: head of the first half
 * @h2: head of the second half
 * Return: 1 if are equals, 0 if not
 */

int compare(listint_t *h1, listint_t *h2)
{
    listint_t *h1;
    listint_t *h2;

    while (h1 != NULL && h2 != NULL)
    {
        if (h1->n == h2->n)
        {
            h1 = h1->next;
            h2 = h2->next;
        }
        else
        {
            return (0);
        }
    }

    if (h1 == NULL && h2 == NULL)
    {
        return (1);
    }

    return (0);
}

/**
 * is_palindrome - checks if a singly linked list
 * is a palindrome
 * @head: pointer to head of list
 * Return: 0 if it is not a palindrome,
 * 1 if it is a palndrome
 */
int is_palindrome(listint_t **head)
{
    listint_t *slow, *fast, *prev_slow;
    listint_t *scn_half, *middle;
    int isp;

    slow = fast = prev_slow = *head;
    middle = NULL;
    isp = 1;

    if (*head != NULL && (*head)->next != NULL)
    {
        while (fast != NULL && fast->next != NULL)
        {
            fast = fast->next->next;
            prev_slow = slow;
            slow = slow->next;
        }

        if (fast != NULL)
        {
            middle = slow;
            slow = slow->next;
        }

        scn_half = slow;
        prev_slow->next = NULL;
        reverse(&scn_half);
        isp = compare(*head, scn_half);

        if (middle != NULL)
        {
            prev_slow->next = middle;
            middle->next = scn_half;
        }
        else
        {
            prev_slow->next = scn_half;
        }
    }

    return (isp);
}
