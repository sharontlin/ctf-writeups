## Invite

I first checked the source code and found a file named /js/inviteapi.min.js. This gave me the following code:

```
eval(function(p,a,c,k,e,d){e=function(c){return c.toString(36)};if(!''.replace(/^/,String)){while(c--){d[c.toString(a)]=k[c]||c.toString(a)}k=[function(e){return d[e]}];e=function(){return'\\w+'};c=1};while(c--){if(k[c]){p=p.replace(new RegExp('\\b'+e(c)+'\\b','g'),k[c])}}return p}('1 i(4){h 8={"4":4};$.9({a:"7",5:"6",g:8,b:\'/d/e/n\',c:1(0){3.2(0)},f:1(0){3.2(0)}})}1 j(){$.9({a:"7",5:"6",b:\'/d/e/k/l/m\',c:1(0){3.2(0)},f:1(0){3.2(0)}})}',24,24,'response|function|log|console|code|dataType|json|POST|formData|ajax|type|url|success|api|invite|error|data|var|verifyInviteCode|makeInviteCode|how|to|generate|verify'.split('|'),0,{}))
```

I used a Javascript compiler (learned some neat things about radix used in the toString() method in Javascript) to translate it to following:

```
function verifyInviteCode(code){
    var formData={"code":code};
    $.ajax({
        type:"POST",
        dataType:"json",
        data:formData,
        url:'/api/invite/verify',
        success:function(response){
            console.log(response)
        },
        error:function(response){
            console.log(response)}
    })
}

function makeInviteCode(){
    $.ajax({
        type:"POST",
        dataType:"json",
        url:'/api/invite/how/to/generate',
        success:function(response){
            console.log(response)
        },
        error:function(response){
            console.log(response)
        }
    })
}
```

I then ran makeInviteCode() in the console and received this response:

```
Va beqre gb trarengr gur vaivgr pbqr, znxr n CBFG erdhrfg gb /ncv/vaivgr/trarengr
```

The response said that it was ROT13 encrypted (on closer inspection, it seems that the message uses a different encryption protocol each time the function is executed), so I decrypted the message:

```
In order to generate the invite code, make a POST request to /api/invite/generate
```

I then made a POST request to the URL specified and received this encrypted response:

```
{
  "0": 200,
  "success": 1,
  "data": {
    "code": "UVpIR0otTElRU1ItR0pUWEUtUVVLUUEtTU5BRlI=",
    "format": "encoded"
  }
}
```

I decoded the message from Base64 and got the answer!

```
QZHGJ-LIQSR-GJTXE-QUKQA-MNAFR
```
