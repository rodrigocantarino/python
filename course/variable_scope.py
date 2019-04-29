"""
Variables Scope:
Is the region of a computer program where the binding is valid:
where the name can be used to refer to the entity.
Such a region is referred to as a scope block.
In other parts of the program the name may refer to a different entity
(it may have a different binding), or to nothing at all (it may be unbound).

[1] - Global Variables
    - A declaration has global scope if it has effect and can be accessed throughout an entire program.

[2] - Local Variables
    - A declaration has local scope if it has effect and can be accessed only on that block. More sophisticated modular
    programming allows a separate module scope, where names are visible within the module (private to the module)
    but not visible outside it. Within a function, some languages, such as C, allow block scope to restrict scope
    to a subset of a function; others, notably functional languages, allow expression scope, to restrict scope to a
    single expression.

- Declaration
    variable_name = value
    answer_to_the_ultimate_question_of_life_the_universe_and_everything = 42

- Is not necessary to declare the variable data type

"""
