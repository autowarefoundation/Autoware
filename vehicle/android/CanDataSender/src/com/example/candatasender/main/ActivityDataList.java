/*
 * Copyright 2015 Autoware Foundation. All rights reserved.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

package com.example.candatasender.main;

import java.io.*;
import java.util.ArrayList;
import android.os.Bundle;
import android.os.Environment;
import android.app.Activity;
import android.app.AlertDialog;
import android.content.Intent;
import android.content.DialogInterface;
import android.view.View;
import android.widget.AdapterView;
import android.widget.ArrayAdapter;
import android.widget.ListView;
import android.util.Log;
import com.example.candatasender.R;

public class ActivityDataList extends Activity {
	private final String SD_PATH = Environment.getExternalStorageDirectory().getAbsolutePath();
	private final String CL_USB = "carlink_can_usb_accessory/log";
	private final String CL_BT  = "carlink_can_bt/log";
	private final String CG     = "ECS/CanGather/log";
	private String tableName;
	private String logDir;
	private String dstDir;
	private boolean raw;

	@Override
	protected void onCreate(Bundle savedInstanceState) {
		Log.d("MethodCall", "ActivityDataList.onCreate()");
		super.onCreate(savedInstanceState);
		setContentView(R.layout.activity_listview);

		Intent intent = getIntent();
		tableName = intent.getStringExtra("table");
		dstDir    = intent.getStringExtra("dir");
		raw       = intent.getBooleanExtra("raw", true);
	}

	@Override
	protected void onResume() {
		Log.d("MethodCall", "ActivityDataList.onResume()");
		super.onResume();
		initMenu();
	}

	/**
	 * メニュー表示
	 */
	private void initMenu() {
		Log.d("MethodCall", "ActivityDataList.initMenu()");

		//アダプタを設定
		ListView lv = (ListView)findViewById(R.id.lv_menu);
		ArrayAdapter<String> adpt = new ArrayAdapter<String>(this, android.R.layout.simple_list_item_1, logList());
		lv.setAdapter(adpt);

		//リストビューのアイテムがクリックされた際のリスナーの登録
		lv.setOnItemClickListener(new AdapterView.OnItemClickListener() {
			@Override
			public void onItemClick(AdapterView<?> parent, View view, int position, long id) {
				ListView list = (ListView)parent;
				logDir = (String)list.getItemAtPosition(position);
				onClkLog();
			}
		});
	}

	private String[] logList() {
		ArrayList<String> list = new ArrayList<String>();
		File dir;
		File[] files;

		/* CarLink USB */
		dir = new File(SD_PATH + "/" + CL_USB);
		files = dir.listFiles();
		if (files != null) {
			for (File f: files) {
				if (f.isDirectory()) list.add(CL_USB + "/" + f.getName());
			}
		}

		/* CarLink BT */
		dir = new File(SD_PATH + "/" + CL_BT);
		files = dir.listFiles();
		if (files != null) {
			for (File f: files) {
				if (f.isDirectory()) list.add(CL_BT + "/" + f.getName());
			}
		}

		/* CanGather */
		dir = new File(SD_PATH + "/" + CG);
		files = dir.listFiles();
		if (files != null) {
			for (File f: files) {
				if (f.isDirectory()) list.add(CG + "/" + f.getName());
			}
		}

		return list.toArray(new String[list.size()]);
	}

	/**
	 * データがクリックされたとき
	 */
	private void onClkLog() {
		Log.d("MethodCall", "ActivityDataList.onClkLog()");

		AlertDialog.Builder adb = new AlertDialog.Builder(this);
		adb.setTitle(logDir);
		adb.setMessage("データを送信しますか？");
		adb.setPositiveButton("送信", new DialogInterface.OnClickListener() {
			@Override
			public void onClick(DialogInterface dialog, int which) {
				if (raw) {
					sendRawData();
				} else {
					recordTable();
				}
			}
		});
		adb.setNegativeButton("キャンセル", null);
		adb.show();
	}

	/**
	 * テーブル登録
	 */
	private void recordTable() {
		Log.d("MethodCall", "ActivityDataList.recordTable()");

		if (logDir.startsWith(CL_USB)) {
			CarLinkDataSend clds = new CarLinkDataSend(this);
			clds.execute(logDir, dstDir, SD_PATH, "usb", tableName);
		}
		else if (logDir.startsWith(CL_BT)) {
			CarLinkDataSend clds = new CarLinkDataSend(this);
			clds.execute(logDir, dstDir, SD_PATH, "bt", tableName);
		}
		else if (logDir.startsWith(CG)) {
			CanGatherDataSend cgds = new CanGatherDataSend(this);
			cgds.execute(logDir, dstDir, SD_PATH, tableName);
		}
	}

	/**
	 * RAWデータ送信
	 */
	private void sendRawData() {
		Log.d("MethodCall", "ActivityDataList.sendRawData()");

		RawDataScp rds = new RawDataScp(this);
		rds.execute(dstDir, SD_PATH, logDir);
	}
}
