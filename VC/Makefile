CC		= gcc
CFLAGS	= -Wall -Werror -Wextra
NAME	= main
SRCS	= main.c src/*.c

all: $(NAME)

$(NAME): $(OBJS)
	$(CC) $(CFLAGS) $(SRCS) -o $(NAME)

clean:
	/bin/rm -f *.o

fclean: clean
	/bin/rm -f $(NAME)

re: fclean all
