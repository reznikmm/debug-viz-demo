package body Some_Pkg is
   function JSON (Dummy : Integer) return String is
      Text : String :=
         "{ 'kind':{ 'plotly': true }," &
         "'data':[" &
         " { 'y': [1, 2, 4, 8, 16] }," &
         "{ 'y': [14, 3, 0, 15, 10] }" &
         "]}";
   begin
      for X of Text loop
         if X = ''' then
            X := '"';
         end if;
      end loop;
      return Text;
   end JSON;
end Some_Pkg;