#include<stdio.h>
#include<sys/stat.h>
#include<fcntl.h>
#include<unistd.h>
/**
 *main- Copy of archives
 *Return: exit succesfull
 */

int main(int argc, char *argv[])
{
    int fd, num_rc;
	char buff[1024];

	if (argc != 2)
	{
		printf("error\n");
		return (1);
	}
	fd = open(argv[1], O_RDONLY);
	if (fd == -1)
		printf("error\n");

    while ((num_rc = read(fd, buff, 1024)) > 0)
	{
		if (write(STDOUT_FILENO, buff, num_rc) == -1)
		{
			printf("no salio\n");
			return (-1);
		}
	}
	if (close(fd) == -1)
	{
		printf("no se pudo cerrar\n");
		return (-1);
	}

    return (0);
}
