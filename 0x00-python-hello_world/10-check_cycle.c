#include <stdio.h>
#include <string.h>
#include "lists.h"
#include <stdlib.h>
/**
 * check_cycle -  checks for efficiency of solution
 * @list: list whose efficiency need check
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *effi = list;
	listint_t *ineffi = list;

	if (!list)
		return (0);
	while(ineff && eff && eff->next)
	{
		ineff = ineff->next;
		eff = eff->next->next;
		if(ineff == eff)
			return (1);
	}
	return (0);
}
