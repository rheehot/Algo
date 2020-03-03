#정사각형 방
import collections
def isMap(x,y):
    if 0 <= x < N and 0 <= y < N:
        return True
    else:
        return False

def BFS(x,y):
    queue = collections.deque()
    cnt = 0
    queue.append((0,x,y))
    while queue:
        depth,x,y = queue.popleft()
        if cnt < depth:
            cnt = depth
        for dx,dy in [(0,1),(1,0),(-1,0),(0,-1)]:
            nx = x + dx
            ny = y + dy    
            if isMap(nx,ny):
                if mat[nx][ny] - 1 == mat[x][y]:
                    queue.append((depth+1,nx,ny))
    return cnt + 1



T = int(input())
for testcase in range(1,T+1):
    N = int(input())
    mat = [[*map(int,input().split())] for _ in range(N)]
    res = 0
    room = 1001
    for x in range(N):
        for y in range(N):
            temp = BFS(x,y)
            if temp >= res:
                res = temp 
                if room > mat[x][y]:
                    room = mat[x][y]
    print(f"#{testcase} {room} {res}")
"""
1
21
53 423 76 204 251 65 119 27 42 122 277 55 195 256 422 112 30 398 341 144 332 
381 32 19 264 56 286 300 401 213 342 238 135 68 91 161 345 280 416 102 75 392 
299 202 13 336 194 151 133 38 255 158 231 138 236 153 417 335 113 369 134 374 237 
263 80 44 294 377 99 21 1 273 162 327 233 436 252 291 404 104 430 421 433 437 
413 386 399 8 346 159 107 275 61 47 177 397 370 28 176 337 230 358 427 268 130 
424 141 4 408 292 174 200 250 221 324 79 160 311 308 334 396 143 126 90 179 258 
267 321 96 89 287 415 389 439 167 245 431 426 105 353 11 82 356 362 175 123 243 
239 425 40 106 152 16 328 7 272 2 246 136 365 137 241 281 298 70 379 34 293 
383 348 390 97 411 368 214 440 198 350 193 172 31 132 247 223 154 29 139 88 228 
288 432 351 95 312 414 15 261 227 12 265 319 285 186 269 52 58 5 352 235 309 
170 248 117 361 222 156 81 115 64 93 393 340 180 366 373 284 278 142 304 320 441 
23 318 171 376 354 212 17 60 290 148 110 419 74 403 147 405 124 310 114 391 39 
367 271 182 92 49 326 262 317 199 191 347 349 57 218 339 86 18 98 307 189 384 
303 313 125 87 201 51 24 163 270 325 224 207 25 6 282 120 77 279 338 190 306 
208 10 146 45 118 129 216 322 301 314 378 428 59 344 375 217 67 225 360 36 382 
197 364 412 145 438 372 406 363 380 78 429 181 165 400 296 128 330 435 140 100 407 
249 242 206 187 54 20 385 66 48 229 41 183 210 331 329 101 297 46 111 205 62 
420 359 395 253 295 69 155 103 72 333 84 244 215 388 121 323 150 305 73 357 394 
343 164 108 371 240 185 188 63 274 259 192 434 232 266 26 35 149 166 43 260 276 
168 33 289 226 85 410 315 196 409 22 302 203 116 50 71 316 219 211 402 37 83 
234 220 169 109 184 131 387 14 9 178 355 254 127 94 209 418 283 257 157 3 173 
"""