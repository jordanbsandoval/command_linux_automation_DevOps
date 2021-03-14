#include<stdio.h>
#include<sys/stat.h>
#include<fcntl.h>
#include<unistd.h>
#include<stdlib.h>
/**
 *main- Copy of archives
 *Return: exit succesfull
 */

int main(int argc, char *argv[])
{
    int fd, fn, num_rc;
	char buff[1024];

	if (argc != 3)
	{
		printf("error_par\n");
		return (1);
	}
	fd = open(argv[1], O_RDWR);
	fn = open(argv[2], O_CREAT | O_WRONLY, 0600);
	if (fd == -1)
	{
		printf("error\n");
		exit(100);
	}
	if (fn == -1)
	{
		printf("error2\n");
		exit(100);
	}

    while ((num_rc = read(fd, buff, 1024)) > 0)
	{
		if (write(fn, buff, num_rc) == -1)
		{
			printf("no salio\n");
			exit(100);
		}
	}
	if (close(fd) == -1 || close(fn) == -1)
	{
		printf("no se pudo cerrar\n");
		exit(100);
	}

    return (0);
}
