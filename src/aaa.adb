with Ada.Characters.Latin_1;
with Some_Pkg;
with System;
procedure Aaa is
   Text : constant String :=
     "const user = {" & Ada.Characters.Latin_1.LF &
     "  firstName: 'Angela'," & Ada.Characters.Latin_1.LF &
     "  lastName: 'Davis'," & Ada.Characters.Latin_1.LF &
     "}";

   Comment : constant String :=
    "// comment:" & Text;

   type Integer_Array is array (1 .. 5) of Integer;
   List : Integer_Array := (1, 2, 3, 4, 5);

   Link_JSON : constant System.Address := Some_Pkg.JSON'Address;
begin
   for X of List loop
      X := X + 3;
   end loop;
end Aaa;