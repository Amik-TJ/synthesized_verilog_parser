module fa(a, b, cin, s, cout);
    input a, b, cin;
    output s, cout;
    wire x1, x2, x3, x4;
    xor xor1(s, a, b, cin);
    and and1(x2, a, b);
    and and2(x3, b, cin);
    and and3(x4, a, cin);
    or or1(cout, x2, x3, x4);
endmodule