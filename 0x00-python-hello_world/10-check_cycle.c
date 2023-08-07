#include "lists.h"
/**
 * check_cycle-checks if there's a cycle
 * @list:a linked list
 * Return:integer
 */
int check_cycle(listint_t *list)
{
	listint_t *temp1, *temp2;

	temp1 = list;
	temp2 = list;

	while (temp1 -> next)
	{
		temp2 = temp1->next;

		while (temp2 -> next)
		{
			if ((temp2->next) == temp1)
				return(1);
			temp2 = temp2 -> next;
		}
		temp1 = temp1 -> next;
	}
	return (0);
}

