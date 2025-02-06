#include <sys/ioctl.h>
#include "hdr/utils.h"

int	main(void)
{
	bool	alive;
	s_map	map;
    struct winsize w;

    ioctl(STDOUT_FILENO, TIOCGWINSZ, &w);
	map.width = w.ws_col;
	map.height = w.ws_row;
	map.framerate = 20;
	map.map = create_map(map.width, map.height, true);
	map.delta_map = create_map(map.width, map.height, false);

	tm_clear();
	alive = true;
	while (alive)
	{
		tm_print_map(&map);
		next_step(&map);
		usleep(100 * 1000);
	}

	free_map(&map);
	return (0);
}
