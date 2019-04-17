# Study-RhinoPython  

RhinoPython のメモ  


```
EditPythonScript
>>> Open Editor

RunPythonScript
>>> Run Script, Select File
```

---  

コマンドライン引数というか、実行時の引数的に使える、rs.get なんとか。  

```
rs.GetObject(msg, filter)
```

Filter  

| Value | Description |
| --- | ---|   
| 0            | All objects (default) |
| 1            | Point |
| 2            | Point cloud |
| 4            | Curve |
| 8            | Surface or single-face brep |
| 16           | Polysurface or multiple-face |
| 32           | Mesh |
| 256          | Light |
| 512          | Annotation |
| 4096         | Instance or block reference |
| 8192         | Text dot object |
| 16384        | Grip object |
| 32768        | Detail |
| 65536        | Hatch |
| 131072       | Morph control |
| 134217728    | Cage |
| 268435456    | Phantom |
| 536870912    | Clipping plane |
| 1073741824   | Extrusion |


Ref.  

[https://developer.rhino3d.com/api/RhinoScriptSyntax/#selection-GetObjects](https://developer.rhino3d.com/api/RhinoScriptSyntax/#selection-GetObjects)  
