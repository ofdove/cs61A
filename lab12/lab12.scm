(define (tail-replicate x n) 'YOUR-CODE-HERE
  (define (inner x n so-far)
    (cond
     ((= n 0) so-far)
     (else (inner x (- n 1) (cons x so-far)))))
  (inner x n nil))

(define-macro (def func args body)
  'YOUR-CODE-HERE
  `(define ,func (lambda ,args ,body)))

(define (repeatedly-cube n x)
  (if (zero? n)
      x
      (let ((y (repeatedly-cube (- n 1) x)))
        (* y y y))))
