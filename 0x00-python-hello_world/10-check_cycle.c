#include "lists.h"
/**
 * check_cycle - checks if the linked list has a cycle
 * @list: Address of a list to be checked
 * Return: 1 if founsd cycle and 0 if not
 */
int check_cycle(listint_t *list)
{
	listint_t *fast, *slow;

	slow = list->next;
	fast = list->next->next;
	while (fast &&  slow && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (slow == fast)
			return (1);
	}
	return (0);
}
