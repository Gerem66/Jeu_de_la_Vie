#ifndef UTILS_H
#define UTILS_H

#include <stdio.h>	// printf (TESTS)
#include <time.h>	// time
#include <unistd.h>	// write, usleep
#include <stdlib.h>	// malloc, free

#define bool	unsigned short
#define false	0
#define true	1

typedef struct t_map
{
	int	width;
	int	height;
	int	framerate;
	int	**map;
	int	**delta_map;
} 		s_map;


char	*ft_itoa(int n);
int		ft_count_digits(int n);
size_t	ft_strlcpy(char *dst, const char *src, size_t dstsize);
void	gotoxy(int x, int y);

void	tm_clear(void);
void	tm_print_map(s_map *map);
int		**create_map(int width, int height, bool random);
int		check_around(int x, int y, s_map *map);
void	next_step(s_map *map);
void	free_map(s_map *map);

#endif /* UTILS_H */
