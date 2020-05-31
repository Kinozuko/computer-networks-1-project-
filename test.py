from PVS.PVS import PVS

record = PVS()
#play = PVS(input=0)

record.start_stream()

frames_bit = record.convert_to_bin(record.record())
fill_bits_frames = []

for fbits in frames_bit:
    fill_bits_frames.append(record.fill_bits(fbits))

fill_bits_bytes_frames = []

for fbits in fill_bits_frames:
    fill_bits_bytes_frames.append(bytes(fbits,"utf-8"))

print(fill_bits_bytes_frames)