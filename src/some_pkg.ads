package Some_Pkg is
   function JSON (Dummy : Integer) return String
     with Export, External_Name => "something";
end Some_Pkg;