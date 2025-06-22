#lang racket
(cons 'car '+)
(list 'esto '(es muy facil))
(cons 'pero '(se esta complicando..)) (cons '(y ahora no se que) 'hizo)
(quote (+ 7 2))

(cons '+ '(10 3)) (car '(+ 10 3)) 
(cdr '(+ 10 3)) 
cons 
(quote (cons(car (cdr (7 4)))) )
(quote cons)
(car (quote (quote cons)))

(+ '2 '3)

(+ (car '(2 3)) (car (cdr '(2 3))))
((car (list + - * /)) 2 3)
(cons 3 '(2))