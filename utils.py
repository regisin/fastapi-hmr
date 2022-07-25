reloader = """
<script>
(() => {
    const socketUrl = "ws://localhost:8000/ws";
    var ws = new WebSocket(socketUrl);
    /*
    * Hot Module Reload
    */
    ws.addEventListener('close',() => {
        console.log('[WS:close]', 'HMR websocket closed.');

        const interAttemptTimeoutMilliseconds = 100;
        const maxAttempts = 5;
        let attempts = 0;
        const reloadIfCanConnect = () => {
            attempts++ ;
            if(attempts > maxAttempts){
                console.error('[WS:error]', 'HMR could not reconnect to dev server.');
                return;
            }
            socket = new WebSocket(socketUrl);
            socket.addEventListener('error',()=>{
                setTimeout(reloadIfCanConnect,interAttemptTimeoutMilliseconds);
            });
            socket.addEventListener('open',() => {
                location.reload();
            });
        };
        reloadIfCanConnect();
    });
})();
</script>
"""
