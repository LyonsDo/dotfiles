;========================
;; Global configuration
;;========================

;;{{{ Text editing

;; Copy, paste cut (CUA mode)
;; (cua-mode t)

;; Auto-Fill Mode
(add-hook 'text-mode-hook 'turn-on-auto-fill)

;; Parens mode
(add-hook 'text-mode-hook 'show-paren-mode)

;; SkeletonMode
;; -------------
;; (setq skeleton-pair t)
;; (global-set-key "(" 'skeleton-pair-insert-maybe)          
;; (global-set-key "{" 'skeleton-pair-insert-maybe)
;; (global-set-key "[" 'skeleton-pair-insert-maybe)

;; CopyFromAbove
;; ---------------
(autoload 'copy-from-above-command "misc"
    "Copy characters from previous non-blank line, starting just above point."
  'interactive)

(global-set-key (kbd "C-c u") 'copy-from-above-command)

(global-set-key (kbd "C-<tab>") 'indent-relative)

;;}}}

;; Ido Mode
(require 'ido-vertical-mode)
(ido-mode t)
(ido-vertical-mode 1)
(setq ido-case-fold t)

;(ido-everywhere t) ; unpleasant with mu4e

;;{{{ Appearance 

;; Frame (window) title

(setq frame-title-format "%b")

;; Fringe
(set-face-background 'fringe "black")

;; Fonts
(set-face-attribute 'default nil :height 150)


;; Themes
;; -------

;; color-theme package

(color-theme-initialize)
(color-theme-goldenrod)
;;(color-theme-lethe)

;; external themes 

;;(add-to-list 'custom-theme-load-path (expand-file-name "underwater-theme.el" themes-dir))
;;(load-theme 'underwater t)

;;(load-theme 'zenburn t)
;(load-theme 'blackboard t)
;(load-theme 'tangotango t)

;;}}}

;;{{{ Key-bindings

;; Rebind "Set mark"
(global-set-key (kbd "M-SPC") 'set-mark-command)

;;(global-set-key (kbd "<f1>") 'save-buffer)

;;(global-set-key (kbd "C-;") 'isearch-forward)
;;(define-key isearch-mode-map (kbd "C-;") 'isearch-repeat-forward)

;; (defun en-us-keymap ()
;;   (local-set-key (kbd "9") '(lambda () (interactive) (insert "(")))
;;   (local-set-key (kbd "0") '(lambda () (interactive) (insert ")")))

;;   (local-set-key (kbd "(") '(lambda () (interactive) (insert "9")))
;;   (local-set-key (kbd ")") '(lambda () (interactive) (insert "0")))
;; )

;; (defun es-latam-keymap ()
;;   (local-set-key (kbd "8") '(lambda () (interactive) (insert "(")))
;;   (local-set-key (kbd "9") '(lambda () (interactive) (insert ")")))

;;   (local-set-key (kbd "(") '(lambda () (interactive) (insert "8")))
;;   (local-set-key (kbd ")") '(lambda () (interactive) (insert "9")))
;; )

;; (add-hook 'emacs-lisp-mode-hook 'es-latam-keymap)

;;}}}

;;{{{ Saner defaults

;; Answer y instead of yes
(defalias 'yes-or-no-p 'y-or-n-p)

;; Save all backup files in a directory
(setq backup-directory-alist '(("." . "~/.emacs.d/backups")))

(global-auto-revert-mode 1)
(setq auto-revert-verbose nil)

;; Conflicts with ebib
;;
;; (defadvice split-window (after move-point-to-new-window activate)
;;   "Moves the point to the newly created window after splitting."
;;   (other-window 1))

;; Completion-ignore-case
(setq read-buffer-completion-ignore-case t)
(setq read-file-name-completion-ignore-case t)

;;}}}

;;{{{ Focus help/doc buffers
;; ------------------------
(defun mb-jump-to-help ()
  "Focus cusor on the help-mode buffer."
  (unless (eq major-mode 'help-mode)
    (other-window 1)))

(defadvice describe-mode (after jump-to-help)
  (mb-jump-to-help))

(defadvice describe-bindings (after jump-to-help)
  (mb-jump-to-help))

(defadvice describe-function (after jump-to-help)
  (mb-jump-to-help))

(defadvice describe-variable (after jump-to-help)
  (mb-jump-to-help))

(defadvice describe-key (after jump-to-help)
  (mb-jump-to-help))

(ad-activate 'describe-mode)
(ad-activate 'describe-bindings)
(ad-activate 'describe-function)
(ad-activate 'describe-variable)
(ad-activate 'describe-key)

;;}}}

;; Insert file path in current buffer
;; -----------------------------------
(defun insert-path (file)
  "insert file path"
  (interactive "FPath: ")
  (insert (expand-file-name file)))

(setenv "PATH"
	(concat
	 "/home/marduk/bin" ":"
	 (getenv "PATH")
))

(provide 'mb-global)
