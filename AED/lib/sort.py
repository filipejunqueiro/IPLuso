from typing import Optional, TypeVar

T = TypeVar("T", int, float, str)

class Sort:
    # O(n²) | Ω(n²) | Θ(n²)
    @staticmethod
    def Selection(target_list: list[T], targe_iter: Optional[int] = None, print_states: bool = False) -> int:
        swaps = 0
        
        for i in range(target_list.__len__()):
            if targe_iter is not None and targe_iter == i:
                break
            
            min_value_index = i

            for j in range(i + 1, target_list.__len__()):
                if target_list[j] < target_list[min_value_index]:
                    min_value_index = j

            swaps += 1
            target_list[i], target_list[min_value_index] = target_list[min_value_index], target_list[i]
            
            if print_states:
                print(target_list)

        return swaps
    
    # O(n²) | Ω(n) | Θ(n²)
    @staticmethod
    def Insertion(target_list: list[T], targe_iter: Optional[int] = None, print_states: bool = False) -> int:
        swaps = 0

        for i in range(1, target_list.__len__()):
            if targe_iter is not None and targe_iter == i-1:
                break

            key = target_list[i]
            j = i - 1

            while j >= 0 and target_list[j] > key:
                swaps += 1
                target_list[j + 1] = target_list[j]
                j -= 1
            
            target_list[j + 1] = key
            
            if print_states:
                print(target_list)

        return swaps