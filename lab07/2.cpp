#include <iostream>


int main(){
	int x = 6, y = 4, z = 8;
	{
		x = x + 1;
		z = z + 2*x + 3*y;
		y = y + 1;

		std::cout << x << " " << y << " " << z << "\n";
	}
	{
		int x = 6, y = 4, z = 8;
		x += 1, z += 2 * x + 3 * y, y += 1;
		std::cout << x << " " << y << " " << z << "\n";
	}
	{
		int x = 6, y = 4, z = 8;
		x++, z += 2 * x + 3 * y, y++;
		std::cout << x << " " << y << " " << z << "\n";
	}
	{
		int x = 6, y = 4, z = 8;
		z += 2 * ++x + 3 * y++;
		std::cout << x << " " << y << " " << z;
	}

	return 0;
}
