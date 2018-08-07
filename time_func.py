# Decorator for timing

import datetime

def time_func(function):
  """ This decorator calculates the amount of time a function takes to execute.

  When time_func is applied to a function it records how long the function takes to
  finish and add the elapsed time to the functions attributes.

  - **parameters**
  :param function: The function you want to add the elapsed time attribute to.

  :Example:
  @time_func
  def example(name, **kwargs):
    meta = type(name, (object,), kwargs)
    return meta

  example('foo')
  print example.elapsed
  0:00:00.000052

  """
  def new_func(*args, **kwargs):
    # Start the clock.
    start = datetime.datetime.now()
    # Execute the function and record the results.
    function_result = function(*args, **kwargs)
    # Calculate the elapsed time and add it to the function
    # attributes.
    new_func.elapsed = datetime.datetime.now() - start
    # Returned the function with the added elapsed attribute
    return function_result
  return new_func
