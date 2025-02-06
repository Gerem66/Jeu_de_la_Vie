#include "../hdr/utils.h"

void	tm_clear(void)
{
	write(1, "\e[1;1H\e[2J", 10);
}

void	gotoxy(int x, int y)
{
	write(1, "\033[", 2);
	write(1, ft_itoa(y), ft_count_digits(y));
	write(1, ";", 1);
	write(1, ft_itoa(x), ft_count_digits(x));
	write(1, "H", 1);
}

void	tm_print_map(s_map *map)
{
	int	x;
	int	y;

	y = 0;
	while (y < map->height)
	{
		x = 0;
		while (x < map->width)
		{
			if (!!map->delta_map[x][y])
			{
				gotoxy(x, y);
				if (!!map->map[x][y])
					write(1, "█", 4);
				else
					write(1, " ", 1);
			}
			x++;
		}
		y++;
	}
}

int	**create_map(int width, int height, bool random)
{
	int	**map;
	int	x;
	int	y;

	if (random)
		srand(time(NULL));
	x = 0;
	map = malloc(width * sizeof(*map));
	if (map == NULL)
	{
		printf("Malloc failed!\n");
		exit(1);
	}
	while (x < width)
	{
		y = 0;
		map[x] = malloc(height * sizeof(*map));
		if (map[x] == NULL)
		{
			printf("Malloc failed!\n");
			exit(1);
		}
		while (y < height)
			map[x][y++] = random ? rand() % 2 : 0;
		x++;
	}

	return (map);
}

int	check_around(int x, int y, s_map *map)
{
	int	cells_around;

	cells_around = 0;
	if (x <= 0 || x >= map->width - 1 || y <= 0 || y >= map->height)
		return (0);

	// Top
	if (!!map->map[x - 1][y - 1]) cells_around++;
	if (!!map->map[x][y - 1]) cells_around++;
	if (!!map->map[x + 1][y - 1]) cells_around++;
	// Left & right
	if (!!map->map[x - 1][y]) cells_around++;
	if (!!map->map[x + 1][y]) cells_around++;
	// Bottom
	if (!!map->map[x - 1][y + 1]) cells_around++;
	if (!!map->map[x][y + 1]) cells_around++;
	if (!!map->map[x + 1][y + 1]) cells_around++;

	return (cells_around);
}

void	next_step(s_map *map)
{
	int	**new_map;
	int	x;
	int	y;

	x = 0;
	new_map = create_map(map->width, map->height, false);
	while (x < map->width)
	{
		y = 0;
		while (y < map->height)
		{
			if (((check_around(x, y, map) == 2 || check_around(x, y, map) == 3) && !!map->map[x][y])
				|| (!map->map[x][y] && check_around(x, y, map) == 3))
				new_map[x][y] = 1;
			map->delta_map[x][y] = map->map[x][y] == new_map[x][y] ? 0 : 1;
			y++;
		}
		x++;
	}

	free_map(map);
	map->map = new_map;
}

void	free_map(s_map *map)
{
	free(map->map);
	//free(map->delta_map); // Why this line crash...
}
