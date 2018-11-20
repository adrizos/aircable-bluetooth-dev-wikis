@ERASE

@INIT 50
0 REM debugging information will be dumped to the SERIAL port
50 Z = 0
51 J = 20
52 A = pioset J
53 RETURN

@IDLE 100
100 A = slave 5
101 A = pioset J
102 A = pioclr J
103 RETURN

@SLAVE 150
150 A = pioset J
151 ALARM 1
152 PRINTS"Welcome, press h"
153 PRINTS" to see the list o 
154 PRINTS"f commands\n\r
155 PRINTS"COMMAND > "
156 RETURN

0 REM this function reads a character and stores it on E

@ALARM 200
200 TIMEOUTS 5
201 INPUTS $0
202 A = strlen $0
203 IF A > 0 THEN 210
204 ALARM 1
205 RETURN

207 ALARM 1
208 PRINTS"COMMAND > "
209 RETURN

0 REM this is the command dispatcher
0 REM help
210 IF $0[0] = 104 THEN 250
0 REM turn on a PIO
211 IF $0[0] = 111 THEN 270
0 REM turn off a PIO
212 IF $0[0] = 102 THEN 275
0 REM read a PIO
213 IF $0[0] = 114 THEN 280
0 REM read digital line
214 IF $0[0] = 100 THEN 290
0 REM close connection
215 IF $0[0] = 99 THEN 295
216 PRINTS"Invalid Command\n\r
217 GOTO 207

0 REM This is the help command
0 REM h help
0 REM o turn on a PIO
0 REM f turn off a PIO
0 REM r read a PIO
0 REM d read digital line
0 REM c close connection
250 PRINTS"h help\n\ro turn on
251 PRINTS" a PIO\n\rf turn of
252 PRINTS"f a PIO\n\rr read a
253 PRINTS" PIO\n\rd read digi
254 PRINTS"tal line\n\rc close
255 PRINTS" connection\n\r
256 GOTO 207

0 REM turn on a PIO
260 PRINTS"Enter the PIO "
261 PRINTS"Number: "
262 INPUTS $0
263 A = atoi $0
264 RETURN

270 GOSUB 260
271 B = pioset A
272 GOTO 207

275 GOSUB 260
276 B = pioclr A
277 GOTO 207

280 GOSUB 260
281 B = pioget A
282 PRINTS"VALUE: "
283 PRINTS B
284 PRINTS"\n\r
285 GOTO 207

290 A = nextsns 1
291 RETURN

295 PRINTS"Bye Bye\n\r"
296 A = disconnect 0
297 A = slave 1
298 RETURN

@SENSOR 300
300 PRINTS"\n\rSENSOR"
301 PRINTS" READING: "
302 A = sensor $0
303 PRINTS $0
304 PRINTS "\n\r
305 ALARM 3 
306 GOTO 208

