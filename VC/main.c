#include "hdr/utils.h"

int	main(void)
{
	bool	alive;
	s_map	map;

	map.width = 80;
	map.height = 30;
	map.framerate = 20;
	map.map = create_map(map.width, map.height, true);

	alive = true;
	while (alive)
	{
		tm_clear();
		tm_print_map(&map);
		next_step(&map);
		usleep(10 * 1000);
	}

	free_map(&map);
	return (0);
}