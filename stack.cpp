#include <iostream>

using namespace std;

class stack{
    public:
    stack();
    stack(stack *s, int max);
    private:
    int max;
    stack *s;

};