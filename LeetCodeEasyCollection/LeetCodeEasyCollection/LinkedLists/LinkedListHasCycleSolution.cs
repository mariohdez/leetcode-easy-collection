﻿using System;
using LeetCodeEasyCollection.DataStructures;

namespace LeetCodeEasyCollection.LinkedLists;

public class LinkedListHasCycleSolution
{
	public bool HasCycle(ListNode head)
	{
		if (head == null) return false;

		ListNode slow = head;
		ListNode fast = head.next;

		while (fast != slow)
		{
			if (fast == null || fast.next == null)
			{
				return false;
			}

			slow = slow.next;
			fast = fast.next.next;
		}

		return true;
	}
}

