#ifndef LISTS_H
#define LISTS_H

#include <stdlib.h>

#define fi if
#define __local __attribute__((weak))

typedef unsigned int uint;

/**
 * enum rets - yes no values
 * @yes: 1
 * @no: 0
 */
enum rets
{
	no,
	yes
};

/**
 * struct listint_s - singly linked list
 * @n: integer
 * @next: points to the next node
 *
 * Description: singly linked list node structure
 * for project
 */
typedef struct listint_s
{
	int n;
	struct listint_s *next;
} listint_t;

/**
 * len - find size of a list
 * @ls: list
 * Return: len
 */
__local uint len(listint_t *ls)
{
	uint i;

	for (i = 0; ls; i++)
		ls = ls->next;

	return (i);
}

size_t print_listint(const listint_t *h);
listint_t *add_nodeint_end(listint_t **head, const int n);
void free_listint(listint_t *head);

int is_palindrome(listint_t **head);

#endif /* LISTS_H */
