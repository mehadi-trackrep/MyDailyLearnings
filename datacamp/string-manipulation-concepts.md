## String Manipulation
An example string - `my_string = "Today is my best day"`
* indexing
  - my_string[3]    => output: `a`
* slicing ([inclusive:exclusive])
  - my_string[3:8]  => output: `ay is m`
  - my_string[:7]   => output: `Today i`
  - my_string[7:]   => output: `s my best day`
* stride
  - my_string[0:8:2]    => output: `Tdyi`
  - my_string[0:8:3]    => output: `Tai`
  - my_string[0:8:4]    => output: `Ty`
  - my_string[::-1] => output: `ym si yadoT` (reverse)
* 