pragma solidity 0.4.25;

contract LMS{
    
    struct lib{
         string username;
         int bookid;
        
    }
    
    lib l;

    function getdata(string _username,int _bookid) public
    {
        l.username=_username;
        l.bookid=_bookid;
      
    
    }
    function Showdata() view public returns (string, int) {
        return (l.username, l.bookid);
    }
}
    
