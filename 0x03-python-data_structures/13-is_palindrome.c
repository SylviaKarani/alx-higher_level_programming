#include "lists.h"

/**
 * is_palindrome - check if a list is a palindrom
 * @head: list
 * Return: yes ? 1 : 0
 */
int is_palindrome(listint_t **head)
{
	listint_t *temp = *head;
	uint size, i;
	int data[10240];

	/* No List */
	fi(!head) return (no);
	/* Empty list */
	fi(!*head) return (yes);

	size = len(temp);

	fi(size == yes) return (yes);

	temp = *head;
	for (i = 0; temp; i++, temp = temp->next)
		data[i] = temp->n;

	for (i = 0; i <= size / 2; i++)
		fi(data[i] != data[size - i - 1]) return (no);

	return (yes);
}
