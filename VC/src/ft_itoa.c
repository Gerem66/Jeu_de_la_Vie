#include <stdlib.h>	// malloc, free

size_t	ft_strlcpy(char *dst, const char *src, size_t dstsize);

static int	ft_pow(int n, size_t p)
{
	int	tmp;

	if (p == 0)
		return (1);
	tmp = n;
	while (p-- > 1)
		n *= tmp;
	return (n);
}

int	ft_count_digits(int n)
{
	unsigned int	i;
	unsigned int	digits;

	i = 0;
	digits = 0;
	if (n < 0)
		n *= -1;
	else if (n == 0)
		return (1);
	if (n >= 2000000000)
		return (10);
	while (ft_pow(10, i++) <= n && ft_pow(10, i) > 0)
		digits++;
	if (digits > 10)
		digits = 10;
	return (digits);
}

static char	*ft_itoa_print_minimum(void)
{
	char	*str_number;

	str_number = malloc(12 * sizeof(char));
	if (str_number == NULL)
		return (NULL);
	ft_strlcpy(str_number, "-2147483648", 12);
	return (str_number);
}

char	*ft_itoa(int n)
{
	size_t	i;
	size_t	size;
	char	*str_number;

	if (n == -2147483648)
		return (ft_itoa_print_minimum());
	i = 0;
	size = ft_count_digits(n);
	if (n < 0)
		size++;
	str_number = malloc((size + 1) * sizeof(char));
	if (str_number == NULL)
		return (NULL);
	if (n < 0)
	{
		str_number[i++] = '-';
		n *= -1;
	}
	while (i < size)
	{
		str_number[i] = ((n / ft_pow(10, size - i - 1)) % 10) + 48;
		i++;
	}
	str_number[i] = '\0';
	return (str_number);
}
