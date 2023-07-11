size(S) :- input(1,1,S).
colors(C) :- input(1,2,C).
button(X-1,Y,C) :- input(X,Y,C), X > 1.

max_steps(S*S/2) :- size(S).

{step(1..S)} :- max_steps(S).
:- step(S), S > 1, not step(S-1).

button(X,Y,C,0) :- button(X,Y,C).

selector(0,1).
selector(1,0).
selector(1,1).
selector(1,-1).
{pair((X,Y), (X+(D*SX),Y+(D*SY)), S)} :-
    selector(SX,SY), step(S);
    button(X,Y,C,S-1);
    size(SIZE), D = 1..SIZE-1, button(X+(D*SX),Y+(D*SY),C,S-1);
    #count{D' : D' = 1..D-1, button(X+(D'*SX),Y+(D'*SY),C',S-1), C' != C} = 0.
:- step(S), #count{FROM, TO : pair(FROM, TO, S)} != 1.

cut(X,Y..Y',S) :- pair((X,Y), (X,Y'), S), Y < Y'.
cut(X..X',Y,S) :- pair((X,Y), (X',Y), S), X < X'.
cut(X+L,Y+L,S) :- pair((X,Y), (X',Y'), S), X < X', Y < Y', L = 0..X' - X.
cut(X+L,Y-L,S) :- pair((X,Y), (X',Y'), S), X < X', Y > Y', L = 0..X' - X.

button(X,Y,C,S) :- button(X,Y,C,S-1), step(S), not cut(X,Y,S).

:- button(_,_,_,S), not step(S+1).



output(1,1,S) :- S = #count{A,B,T : pair(A,B,T)}.
output(T+1,1,X) :- pair((X,Y), (X',Y'), T).
output(T+1,2,Y) :- pair((X,Y), (X',Y'), T).
output(T+1,3,X') :- pair((X,Y), (X',Y'), T).
output(T+1,4,Y') :- pair((X,Y), (X',Y'), T).


