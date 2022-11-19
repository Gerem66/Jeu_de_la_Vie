/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strlcpy.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: glecapla <glecapla@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2022/10/17 13:01:40 by glecapla          #+#    #+#             */
/*   Updated: 2022/10/17 13:06:57 by glecapla         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "util.h"

size_t	ft_strlcpy(char *dst, const char *src, size_t dstsize)
{
	size_t	i;

	i = 0;
	while (*src != '\0' && ++i < dstsize)
		*dst++ = *src++;
	if (i <= dstsize)
		*dst = '\0';
	if (*src != '\0')
		while (*++src != '\0')
			i++;
	return (i);
}
