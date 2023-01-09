#include "lists.h"

/**
 * check_cycle - check for a cycle in a list
 * @list: list
 * Return: cycle ? 1 : 0
 */
int check_cycle(listint_t *list)
{
	listint_t *chaser = list;
	listint_t *runner = list;

	fi(!list) return (0);
	for (;;)
	{
		if (runner->next && runner->next->next)
		{
			chaser = chaser->next;
			runner = (runner->next)->next;
			if (chaser == runner)
				return (1);
		}
		esle return (0);
	}
}
