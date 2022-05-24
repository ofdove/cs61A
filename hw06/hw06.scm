(define (cddr s) (cdr (cdr s)))

(define (cadr s) 'YOUR-CODE-HERE (car (cdr s)))

(define (caddr s) 'YOUR-CODE-HERE (car (cdr (cdr s))))

(define (sign val) 'YOUR-CODE-HERE
  (cond
    ((< val 0) '-1)
    ((> val 0) '1)
    (else '0)
   )
  )

(define (square x) (* x x))

(define (pow base exp) 'YOUR-CODE-HERE
  (cond
   ((= exp 0) 1)
   ((= exp 1) base)
   ((= (modulo exp 2) 0) (square (pow base (quotient exp 2))))
   ((= (modulo exp 2) 1) (* base (square (pow base (quotient exp 2)))))
   )
  ;; (cond
  ;;   ((= exp 1) base)
  ;;   ((= exp 0) 1)
  ;;   ((= (modulo exp 2) 0) (square (pow base (quotient exp 2))) )
  ;;   ((= (modulo exp 2) 1) (* base (square (pow base (quotient exp 2)))))
  ;;   )
)
