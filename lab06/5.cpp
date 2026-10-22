#include <iostream>
#include <string>
namespace hello{
    std::string s = "Hello World!";
    void print(){
        std::cout << "Hi: " << s << '\n';
    }
}

namespace bye{
    std::string s = "Bye World!";
    void print(){
        std::cout << "Bye: " << s << '\n';
    }
}

int main(){
    hello::print();
    bye::print();

    std::cout << hello::s << ' '<<  bye::s << '\n';

    return 0;
}
