import uuid

dtsx_content = f"""<DTS:Executable xmlns:DTS="www.microsoft.com/SqlServer/Dts">
  <DTS:Property DTS:Name="DTSID">{{{uuid.uuid4()}}}</DTS:Property>
  <DTS:Property DTS:Name="CreationDate">2025-08-25T15:00:00</DTS:Property>
</DTS:Executable>
"""

with open("package.dtsx", "w", encoding="utf-8") as f:
    f.write(dtsx_content)

print("package.dtsx generated with new GUID")
