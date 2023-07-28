#include <stdio.h>
#include <stdlib.h>
#include <sys/wait.h>
#include <sys/types.h>
#include <unistd.h>
/**
 * infinite_while - run an infinite while loop
 * Return: Always a success 0
*/
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
 * main - creates five zombie processes
 * Return: 0 a success
*/
int main(void)
{
	pid_t process;
	int counter = 0;

	while (counter < 5)
	{
		process = fork();
		if (process > 0)
		{
			printf("Zombie process created, PID: %d\n", process);
			sleep(1);
			counter++;
		}
		else
			exit(0);
	}
	infinite_while();

	return (0);
}
